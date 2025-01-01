const menu = {
    _courses: {
      appetizers:[],
      mains:[],
      desserts:[],
    },
    get appetizers() {
      return this._courses.appetizers;
    },
     get mains() {
      return this._courses.mains;
    },
     get desserts() {
      return this._courses.desserts;
    },
    set appetizers(appetizers) {
    this._courses.appetizers = appetizers;
    },
    set mains(mains) {
    this._courses.mains = mains;
    },
    set desserts(desserts) {
    this._courses.desserts = desserts;
    },
    get courses() {
      return {
        appetizers: this.appetizers,
        mains: this.mains,
        desserts: this.desserts,
      };
    },
    addDishToCourse(courseName, dishName, dishPrice) {
      const dish = {
        name: dishName,
        price: dishPrice
      };
      return this._courses[courseName].push(dish);
    },
    getRandomDishFromCourse(courseName) {
      const dishes = this._courses[courseName];
      const randomIndex = Math.floor(Math.random() * dishes.length)
      return dishes[randomIndex];
    },
    generateRandomMeal(){
      const appetizer = this.getRandomDishFromCourse('appetizers');
      const main = this.getRandomDishFromCourse('mains');
      const dessert = this.getRandomDishFromCourse('desserts');
      const totalPrice = appetizer.price + main.price + dessert.price;
      
      return `Your meal is ${appetizer.name}, ${main.name}, ${dessert.name} the price is $${totalPrice}.`;
    }
  };
  
menu.addDishToCourse('appetizers', 'Nachos', 5.65);
menu.addDishToCourse('appetizers', 'Potato Skins', 6.75);
menu.addDishToCourse('appetizers', 'Honey Rolls', 7.55);
menu.addDishToCourse('appetizers', 'Broccoli Potato Soup', 4.55);
menu.addDishToCourse('appetizers', 'Mozzarella sticks', 5.65);
menu.addDishToCourse('appetizers', 'Chips and Salsa', 4.00);
menu.addDishToCourse('appetizers', 'wings', 8.50);

menu.addDishToCourse('mains', 'Variety Ramen', 24.95);
menu.addDishToCourse('mains', 'Burger Variations', 24.95);
menu.addDishToCourse('mains', 'Curry', 10.95);
menu.addDishToCourse('mains', 'Vegetable Chow Mein', 15.95);
menu.addDishToCourse('mains', 'Salisbury Steak', 17.99);
menu.addDishToCourse('mains','Steak', 20.13);
menu.addDishToCourse('mains','Quesadilla', 12.90);
menu.addDishToCourse('mains','Bacon Cheeseburger', 10.90);

menu.addDishToCourse('desserts','Cake',6.20);
menu.addDishToCourse('desserts','Peacan Pie',6.50);
menu.addDishToCourse('desserts', 'Gelato Variations', 8.95);
menu.addDishToCourse('desserts', 'Peacan pie', 8.95);
menu.addDishToCourse('desserts', 'Tea cookies', 10.95);
menu.addDishToCourse('desserts', 'Milkshakes', 5.34);

let meal = menu.generateRandomMeal();
console.log(meal);
