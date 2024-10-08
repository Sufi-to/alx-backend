import { createClient, print } from 'redis';

const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });


const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, res) => {
      if(err) {
        console.log(err);
        throw err;
      };
      console.log(res)
    });
    
    console.log(value); 
}

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
