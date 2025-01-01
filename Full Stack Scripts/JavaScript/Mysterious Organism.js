// Returns a random DNA base
const returnRandBase = () => {
    const dnaBases = ['A', 'T', 'C', 'G']
    return dnaBases[Math.floor(Math.random() * 4)] 
  }
  
  // Returns a random single stand of DNA containing 15 bases
  const mockUpStrand = () => {
    const newStrand = [];
    for (let i = 0; i < 15; i++) {
      newStrand.push(returnRandBase())
    }
    return newStrand
  }
  
  //Solution:
  //Factory function
  function pAequorFactory(num, dnaStrand){
    return {
      Specimen: num,
      dna: dnaStrand,
  //This obj method uses a while loop, which loop an uncertin amount of times until conditon proves true. Selects a random number that will be our random index
      mutate(){
       let randomBase = Math.floor(Math.random() * 15); 
  //returns an array of the bases that match the base found at the random index of the dna array
        let excludedBases = this.dna.filter(base => base === this.dna[randomBase]); 
        let substituteBase = returnRandBase(); //selects a random base
        while (excludedBases.includes(substituteBase)) {
  //while the value selected for the substitute base can be found in the array of bases to exclude, keep on randomly picking one
          substituteBase = returnRandBase(); 
        }
  //removes the randomly chosen current base from the dna array and replaces it with the substitute base
        this.dna.splice(randomBase, 1, substituteBase); 
  
        return this.dna
        },
  
      compareDNA(comparedObj){
  // Compute the percentage of identical bases (same value and index) between the current object's DNA and a passed in object's DNA
        let identicalBases = 0;
          for (let i = 0; i < this.dna.length; i++) {
            for (let j = 0; j < comparedObj.dna.length; j++) {
                if (this.dna[i] === comparedObj.dna[j] && i === j) {
                identicalBases++
              }
            }
          }
          console.log(this.dna);
          console.log(comparedObj.dna);
          console.log(identicalBases);
        let percentage = (identicalBases / 15 * 100).toFixed(2);
        console.log(`Specimen ${this.specimenNum} and Specimen ${comparedObj.specimenNum} have ${percentage}% DNA in common.`);
        },
  
        willLikelySurvive(){
          let charBases = this.dna.filter(base => base === 'C' || base === 'G');
          const percentage = charBases.length / 15 *100;
  
        return `The likely survival rate of this DNA strand is ${percentage.toFixed(2)}%`
        },
  
        complementStrand(){
          let complement = this.dna.map(base => {
           switch (base) {
             case 'A': 
              return 'T';
             case 'T':
              return 'A';
             case 'C': 
              return 'G';
             case 'G':
              return 'C';
           }
          })
          return complement;
       }
   }
  };
  
  
  /**You can learned a lot but barley anything at all.*/
  //console.log(returnRandBase())
  //console.log(mockUpStrand())
  
  /**Test (objs inside Variables) */
  let pA1 = pAequorFactory(2, mockUpStrand());
  let pA2 = pAequorFactory(2, mockUpStrand());
  //console.log(pA1);
  //console.log(pA2);
  //console.log(pA1.compareDNA(pA2));
  //console.log(pA1.mutate());
  //console.log(pA2.willLikelySurvive());
  //console.log(pA1.complementStrand());
  