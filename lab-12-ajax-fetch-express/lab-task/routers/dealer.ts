import {Router} from "express";

// making a 'arena' router
export const dealerRouter = Router();

dealerRouter
    // form to make a fight
    .get('/', async (req, res) => {

    })
    // post to start a fight
    .post('/add', async (req, res) => {

    })
    .delete('/sell', async (req, res) => {

    })

