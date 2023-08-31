const apikey = "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";

function test()
{
    console.log("testr");
    const message = document.getElementById('messageContent').value;
    console.log("Button clicked!!! send");
    sendMessage(message)
};

function sendMessage(message)
{
    console.log(message);
    fetch('https://api.openai.com/v1/engines/davinci-codex/completions',
    {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'Authorization' : `bearer ${apikey}`
        },
        body: JSON.stringify
        ({
            prompt: message,
            max_tokens: 50
        })
    })
    .then(response => response.json())
    .then(data => {
        const botreply = data.choices[0].text;
        displayBotReply(botreply);
    })
     .catch(error => console.error(error));
}

function displayBotReply(reply)
{
    console.log(reply);
}