class Node{
    constructor(val){
        this.val = val
        this.next = null
    }
}

class stack{
    constructor(val){
        const newNode = new Node(val);
        this.top = newNode
        this.length = 1

    }
    print() {
        let temp = this.top;
        let result = [];
        while (temp) {
            result.push(temp.val);
            temp = temp.next;
        }
        console.log(result.join(" -> "));
    }

    push(val){
        const newNode = new Node(val);
        newNode.next = this.top;
        this.top = newNode;
        if (this.length === 0) {
            this.tail = newNode;
        }
        this.length++;
        return this;
    }
    pop(){

    if(!this.top){return undefined}
        let temp = this.top
        this.top = this.top.next
        temp.next = null
        this.length--
        return this

    }


}

let first = new stack(10)
first.push(20)
first.pop()
first.print()