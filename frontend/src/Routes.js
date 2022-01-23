import React from "react";
import {BrowserRouter,Route,Routes as Rts} from 'react-router-dom';

// import { Switch } from "react-router";

import Home from './core/Home'

const Routes = () =>{
    return (
        <BrowserRouter>
            <Rts>
                <Route path='/' exact element={<Home/>}/>
            </Rts>
        </BrowserRouter>
    )
}

export default Routes;