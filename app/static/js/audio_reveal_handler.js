document.getElementById('revealMessageBtn').addEventListener('click', async function (event) {
    event.preventDefault();

    const audioFile = document.getElementById('revealAudioUpload').files[0];

    if (!audioFile) {
        alert('Please provide an audio file');
        return;
    }

    const formData = new FormData();
    formData.append('audio', audioFile);

    try {
        const response = await fetch('/audio/reveal_audio_message', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error('Error processing the audio file. Please try again.');
        }

        const data = await response.json();

        if(data.message){
            const messageElement = document.getElementById('messageDisplay');
            messageElement.textContent = `Secret message: ${data.message}`;
        }
        else{
            throw new Error('No message found in the audio file');
        }
    } catch (error) {
        alert(error.message);
    }
});