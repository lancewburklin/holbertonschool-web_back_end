const express = require('express');
const app = express();
import redis from 'redis';
const client = redis.createClient();
const { promisify } = require('util');
const getAsync = promisify(client.get).bind(client);

const listProducts = [
  {
    Id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    Id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    Id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    Id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  }
]

function getItemById(id) {
  let i = 0;
  for (i = 0; i < listProducts.length; i++) {
    console.log(listProducts[i].Id);
    if (listProducts[i].Id == id) {
      return (listProducts[i])
    }
  }
}

app.get('/list_products', (req, res) => {
  let info = [];
  let i = 0;
  for (i = 0; i < listProducts.length; i++) {
    const obj = {
      "itemId": listProducts[i].Id,
      "itemName": listProducts[i].name,
      "price": listProducts[i].price,
      "initialAvailableQuantity": listProducts[i].stock
    }
    info.push(obj);
  }
  res.send(info);
})

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const cStock = await getCurrentReservedStockById(itemId);
  if (cStock !== null) {
    const item = getItemById(itemId);
    res.send({
      "itemId": item.id,
      "itemName": item.name,
      "price": item.price,
      "initialAvailableQuantity": item.stock,
      "currentQuantity": cStock
    });
  } else {
    res.send({ "status": "Product not found" });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const press = await getCurrentReservedStockById(itemId);
  if (press !== null) {
    if (press == 0) {
      res.send({ "status": "Not enough stock available", "itemId": 1 });
    } else {
      reserveStockById(itemId, press - 1);
      res.send({ "status": "Reservation confirmed", "itemId": itemId });
    }
  } else {
    res.send({"status":"Product not found"});
  }
});

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  return await getAsync(`item.${itemId}`);
}

app.listen(1245, () => {
  reserveStockById(1, 4);
  reserveStockById(2, 10);
  reserveStockById(3, 2);
  reserveStockById(4, 5);
});
