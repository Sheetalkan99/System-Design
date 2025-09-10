class Animal{
    constructor(name){
        this.name = name;
    }
    getAnimal(){
        return this.name;
    }
    setAnimal(name){
        this.name = name;
    }
}

const myAnimal = new Animal("Leo");
