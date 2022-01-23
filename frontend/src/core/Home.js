import React,{useState , useEffect} from "react"
import {Row,Col} from "react-bootstrap"
import Base from "./Base"
import { getProducts } from "./helper/coreApicalls"
import Card from "./Card"



export default function Home(){
    const [products,setProducts] = useState([])
    const [error,setError] = useState(false)

    const loadAllProducts = () =>{
        getProducts()
            .then(data =>{
                if(data.error){
                    setError(data.error)
                    console.log(error);
                }else{
                    setProducts(data);
                }
            })
            .catch(err => console.log(err))
    }

    useEffect(()=>{
        loadAllProducts();
    },[])

    return(
        <Base title="Index Page" description="Welcome To Russain Bottle Store">
            <h3>Home Component</h3>
            <Row>
                {products.map((product,index)=>{
                    return(
                        <span key={index} className="col-4 mb-4">
                            <Card product={product}/>
                        </span>
                    )
                })}
            </Row>
        </Base>
    )
}
