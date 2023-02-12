const http = require('http');
const express = require('express');
const cors = require('cors');
const {Server} = require('socket.io');
const bodyParser = require('body-parser');

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
let PacmanLife = "3";

// app.use((req, res, next) => {
//     res.header("Access-Control-Allow-Origin", "http://127.0.0.1:3000");
//     res.header("Access-Control-Allow-Credentials", true);
//     res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
//     next();
// });

app.use(bodyParser.json());
app.use(express.json());
app.use(cors());



app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "frontend/index.html"));
})

app.post('/', (req, res) => {
    console.log(req.body);
    res.json(req.body);
});

app.get('/data', (req, res) => {
    res.send({
        "score": PacmanScore,
        "life": PacmanLife
    });
});

app.post('/data', (req,res) => {
    PacmanScore = req.body.score
    PacmanLife = req.body.life
    res.send({
        "score":PacmanScore,
        "life":PacmanLife
    });
})  




httpServer.listen(port, () => {
    console.log(`Server started on http://192.168.1.30:${port}`);
});