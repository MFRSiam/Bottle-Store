import React from "react";
import { Card as Cd,Button } from "react-bootstrap";
import ImageHelper from "./helper/imageHelper";

//TOdo Deal With this later

const isAuthenticated = true;
const addToCart = () =>{
    if(isAuthenticated){
        console.log("Added To Cart")
    }else{
        console.log("Login Please")
    }
}

const removeFromCart = ()=>{
    if(isAuthenticated){
        console.log("Removed From Cart")
    }else{
        console.log("Login Please")
    }
}

// const getAredirect = redirect =>{
//     if(redirect){
//         return 
//     }
// }

const showAddToCart = addToCart =>{
    return(
        addToCart && (
            <Button onClick={addToCart} variant="primary m-1">Add To Cart</Button>
        )
    )
}

const showRemoveFromCart = removefromCart =>{
    return(
        removefromCart && (
            <Button onClick={removeFromCart} variant="warning m-1">Remove From Cart</Button>
        )
    )
}

const Card = ({product,addtoCart=true,removefromCart=false}) => {
    const cardTitle = product ? product.name : "A Photo From Error";
    const cardDescription = product ? product.description : "Error Description";
    const cardPrice = product ? product.price : "Default";
    return (
        <Cd>
            <Cd.Header>Featured</Cd.Header>
            <ImageHelper product={product}/>
            <Cd.Body>
                <Cd.Title>{cardTitle}</Cd.Title>
                <Cd.Text>
                    {cardDescription}
                </Cd.Text>
                <Cd.Text>{cardPrice}</Cd.Text>
                {showAddToCart(addToCart)}
                {showRemoveFromCart(removefromCart)}
            </Cd.Body>
        </Cd>
    );
};

export default Card;
