import {Router} from "express";
import {CarRecord} from "../records/car_db";

// making a 'arena' router
export const dealerRouter = Router();

dealerRouter
    // form to make a fight
    .get('/', async (req, res) => {
        const cars = await CarRecord.listAll()
        // console.log(cars)
        res.render('dealer', {cars})
    })
    // post to start a fight
    .post('/add', async (req, res) => {
    })
    .post('/sell', async (req, res) => {
        const {deleteId}=req.body
        const car = await CarRecord.getOneCar(deleteId)
        await car.deleteOne()
        res.redirect('/dealer')
    })