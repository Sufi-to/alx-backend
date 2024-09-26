import { createClient, print } from 'redis';

const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });


  const get = promisify(client.get).bind(client);

  async function displaySchoolValue(schoolName) {
      const res = await client.get(schoolName).catch((error) => {
        if (error) {
          console.log(error);
          throw error;
        }
      });
      console.log(res);
    }

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
