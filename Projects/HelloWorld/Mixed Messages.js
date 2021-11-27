messages = ["This is a message.", "This is another message.", "I'm the sibling of those two messages.", "I'm jeffery."]

function mmixedMessages(arr){
    console.log(arr[Math.floor(Math.random()*(arr.length - 1))]);
    
}

mmixedMessages(messages);