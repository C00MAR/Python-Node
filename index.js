const http = require('http');
const express = require('express');
const cors = require('cors');
const {Server} = require('socket.io');

const app = express();
const port = 3000;
const path = require("path")

const httpServer = http.createServer(app);
const io = new Server(httpServer, {
    cors: {
        origin: "*"
    }
});

let PacmanScore = "0";


app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "frontend/index.html"));
})

app.post('/', (req, res) => {
    console.log(req.body);
    res.json(req.body);
});

app.get('/score', (req, res) => {
    res.send({
    "score": PacmanScore,
    });
});

app.post('/score', (req,res) => {
    PacmanScore = req.body.score
    res.send({"PacmanScore":req.body.score,})
})  

app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "http://127.0.0.1:5500");
    res.header("Access-Control-Allow-Credentials", true);
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.use(express.json());
app.use(cors());


httpServer.listen(port, () => {
    console.log(`Server started on http://localhost:${port}`);
});