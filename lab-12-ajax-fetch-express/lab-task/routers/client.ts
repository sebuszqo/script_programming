import {Router} from "express";
import {UserRecord} from "../records/client_db";
import {CarRecord} from "../records/car_db";
import {type} from "os";
import {log} from "util";

// making a 'arena' router
export const clientRouter = Router();

clientRouter
    // form to make a fight
    .get('/', async (req, res) => {
        const users = await UserRecord.listAll()
        const carsToRender = await CarRecord.listAll()
        console.log(carsToRender)
        const array = []
        for (const user of users) {

            let cars = await CarRecord.getOneCar(user.car)
            array.push({
                car: user.car,
                name: user.name,
                brand: cars.brand,
                model: cars.model,
                year: cars.year,
                num: cars.num
            })
        }
        res.render("client", {array, carsToRender})
    })
    // post to start a fight


