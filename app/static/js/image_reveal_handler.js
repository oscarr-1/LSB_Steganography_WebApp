document.getElementById('revealMessageBtn').addEventListener('click', async function (event){
    event.preventDefault();

    const imageFile = document.getElementById('revealImageUpload').files[0];

    if(!imageFile){
        alert('Please provide an image')
        return;
    }
    
    const formData = new FormData();
    formData.append('image', imageFile)

    try{
        const response = await fetch('/image/reveal_image_message',{
            method: 'POST',
            body: formData,
        });

        if(!response.ok)
            throw new Error('Error processing the image. Please try again.')

        const message = await response.text();

        const messageElement = document.getElementById('messageDisplay');
        messageElement.textContent = `Secret message: ${message}`;
        
    } catch(error){
        alert(error.message);
    }
})