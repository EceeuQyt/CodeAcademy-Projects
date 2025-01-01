let secretMessage = ['Learning', 'is', 'not', 'about', 'what', 'you', 'get', 'easily', 'the', 'first', 'time,', 'it', 'is', 'about', 'what', 'you', 'can', 'figure', 'out.', '-2015,', 'Chris', 'Pine,', 'Learn', 'JavaScript'];

//removes last element of array and prints new length.
secretMessage.pop();
console.log(secretMessage.length);

//In order: adds two elements at the end, changes index #7 element to right, .shift omits first element, .unshift adds element in beginning,.splice start from index #6 omits 4 elements and ends at fifth, then replaces with 'know,'.  
secretMessage.push('to', 'Program');
secretMessage[7] = 'right';
secretMessage.shift();
secretMessage.unshift('Programaing');
secretMessage.splice(6, 5, 'know,');

//.join() method combines all above array methods w/ a space.
console.log(secretMessage.join(' '))
