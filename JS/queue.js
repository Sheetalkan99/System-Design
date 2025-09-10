class Node{
    constructor(val){
        this.val = val
        this.next = null
    }

}

class Queue{
    constructor(val){
        const newNode = new Node(val)
        this.first = newNode
        this.last = newNode
        this.length = 1
    }

    print() {
        let temp = this.first;
        let result = [];
        while (temp) {
            result.push(temp.val);
            temp = temp.next;
        }
        console.log(result.join(" -> "));
    }

    enqueue(val){
        const newNode = new Node(val)
        if(this.length == 0){
            this.first = newNode
            this.last = newNode
        }
        this.last.next = newNode
        this.last = newNode
        this.length ++
        return this
    }
    dequeue(){
        if(this.length == 0){
            return undefined
        }
        if(this.length == 1){
            this.first = null
            this.last = null;
        }
        let temp = this.first
        this.first = temp.next 
        temp.next = null
        this.length --
        return this
    }
}

let first = new Queue(10)
first.enqueue(20)
first.dequeue()
first.print()