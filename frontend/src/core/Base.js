import React from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import {Container} from 'react-bootstrap'


const Base = ({
    title = "My Title",
    description = "My Description",
    className = "bg-dark text-white p-4",
    children
}) => {
    return(
        <div>
            <Header/>
            <Container>
                <main className="py-3">
                    <div className="jumbotron bg-dark text-white text-center">
                        <h3 className="text-white">{title}</h3>
                        <p className="lead">{description}</p>
                    </div>
                    <Container>
                        {children}
                    </Container>
                </main>
            </Container>
            <Footer/>
        </div>
    )
}

export default Base