import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const updateHash = (key, field, value) => {
  client.hset(key, field, value, print);
};

const printHash = (key) => {
  client.hgetall(key, (_, values) => {
    console.log(values);
  });
};

const updateAndPrintHash = () => {
  const hashObj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  for (const [field, value] of Object.entries(hashObj)) {
    updateHash('HolbertonSchools', field, value);
  }
  printHash('HolbertonSchools');
};

client.on('connect', () => {
  console.log('Redis client connected to the server');
  updateAndPrintHash();
});