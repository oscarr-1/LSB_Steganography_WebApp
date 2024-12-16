document.getElementById('hideMessageBtn').addEventListener('click', async function (event) {
    event.preventDefault();

    const message =  document.getElementById('msg').value;
    const imageFile =  document.getElementById('hideImageUpload').files[0];

    if(!message || !imageFile){
        alert('Please provide both a message and an image');
        return;
    }

    const formData = new FormData();

    formData.append('message', message);
    formData.append('image', imageFile);

    try{
        const response = await fetch('/image/hide_image_message', {
            method: 'POST',
            body: formData,
        });

        if(!response.ok){
            throw new Error('Error processing the image. Please try again');
        }

        const blob = await response.blob();
        const downloadUrl = URL.createObjectURL(blob);

        const downloadLink = document.createElement('a');
        downloadLink.href =  downloadUrl;
        downloadLink.download = 'modified_image.jpeg';
        downloadLink.textContent = 'Download Modified Image';

        const container = document.getElementById('result');
        container.appendChild(downloadLink);
    } catch(error){
        alert(error.message);
    }
});