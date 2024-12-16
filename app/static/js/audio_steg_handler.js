document.getElementById('hideMessageBtn').addEventListener('click', async function (event) {
    event.preventDefault();

    const message = document.getElementById('msg').value;
    const audioFile = document.getElementById('hideAudioUpload').files[0];

    if(!message || !audioFile){
        alert('Please provide both a message and an audio file');
        return;
    }

    const formData = new FormData();

    formData.append('message', message);
    formData.append('audio', audioFile);

    try{
        const response = await fetch('/audio/hide_audio_message', {
            method: 'POST',
            body: formData,
        });

        if(!response.ok){
            throw new Error('Error processing the audio file. Please try again.');
        }
        
        const blob = await response.blob();
        const downloadURL = URL.createObjectURL(blob);

        const downloadLink = document.createElement('a');
        downloadLink.href = downloadURL;
        downloadLink.download = 'modified_audio.wav';
        downloadLink.textContent = 'Download Modified Audio';

        const container = document.getElementById('result');
        container.appendChild(downloadLink);
    } catch(error){
        alert(error.message);
    }
});