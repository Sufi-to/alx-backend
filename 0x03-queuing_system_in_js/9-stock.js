import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

const getItemById = (id) => {
  return listProducts.find((product) => product.id === id);
};

const reserveStockById = (itemId, stock) => {
  client.set(`item_${itemId}`, stock);
};

const getCurrentReservedStockById = promisify(client.get).bind(client);

app.get('/list_products', (req, res) => {
  res.json(listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  })));
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }
  const currentStock = await getCurrentReservedStockById(`item_${itemId}`);
  const currentQuantity = currentStock ? parseInt(currentStock) : item.stock;
  res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity,
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }
  const currentStock = await getCurrentReservedStockById(`item_${itemId}`);
  const currentQuantity = currentStock ? parseInt(currentStock) : item.stock;
  if (currentQuantity === 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }
  reserveStockById(itemId, currentQuantity - 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});