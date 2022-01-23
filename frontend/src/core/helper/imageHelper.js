import React from 'react'

const ImageHelper = ({product}) => {
    const imageurl = product ? product.image : `https://image.shutterstock.com/image-illustration/img-file-document-icon-trendy-260nw-1407027353.jpg`

    return(
        <div className='rounded border border-success p-2'>
            <img src={imageurl} style={{maxHeight:"100%",maxWidth:"100%"}} className='mb-3 img-rounded'/>
        </div>
    )
}

export default ImageHelper