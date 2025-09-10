class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor(val) {
        const newNode = new Node(val);
        this.head = newNode;
        this.tail = this.head;
        this.length = 1;
    }

    push(val) {
        const newNode = new Node(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = this.head;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.length++;
        return this;
    }

    pop() {
        if (!this.head) return undefined;

        let temp = this.head;
        let pre = null;

        while (temp.next) {
            pre = temp;
            temp = temp.next;
        }

        this.tail = pre;
        if (pre) {
            this.tail.next = null;
        } else {
            this.head = null;
            this.tail = null;
        }

        this.length--;
        return temp;
    }

    unshift(value) {
        const newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;
        if (this.length === 0) {
            this.tail = newNode;
        }
        this.length++;
        return this;
    }

    shift(value){

        if(!this.head) return undefined;
        let temp = this.head
        this.head = this.head.next
        this.length--
        if(this.length == 0){
            this.tail = null
        }
        temp.next = null
        return temp

    }

    get(index){
        if (index < 0 || index >= this.length) {
            return null; 
        }
    
        let temp = this.head;
        for (let i = 0; i < index; i++) {
            temp = temp.next;
        }
        return temp;
    }

    set(index,val){
        if (index < 0 || index >= this.length) {
            return null; 
        }

        let temp = this.get(index);
        if(temp){
            temp.val = val
            return true
        }
        return false
    }

    insert(index,val){
        let temp = this.get(index - 1);
        const newNode = new Node(val);
        newNode.next = temp.next
        temp.next = newNode
        this.length++

        }
    
    remove(index,val){
        let before = this.get(index - 1);
        let temp = before.next
        before.next = temp.next
        temp.next = null
        this.length--

        
    }

    reverse(){
        let temp = this.head
        this.head = this.tail 
        this.tail = temp
        let prev = null
        let next = temp.next
        for(let i = 0 ; i < this.length; i++){
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        }
    }
      
    print() {
        let temp = this.head;
        let result = [];
        while (temp) {
            result.push(temp.val);
            temp = temp.next;
        }
        console.log(result.join(" -> "));
    }

    /*
    middleelement() {
        if (this.length === 0) return null; // Handle empty list
    
        let midIndex = Math.floor(this.length / 2); // Get middle index
        return this.get(midIndex); // Return the node at middle index
    }
    */
   middleelement(){
    let slow = this.head
    let fast = this.head
    while(fast!== null && fast.next!== null){
        slow = slow.next ;
        fast = fast.next.next;
        
    }
    return slow;
    
   }
   //Reverse Linked List
   reverselist(){
        let temp = this.head
        this.head = this.tail
        this.tail = temp 
        let prev = null 
        let next = temp.next 
        for(let i = 0; i < this.length; i ++ ){
            next = temp.next 
            temp.next = prev
            prev = temp
            temp = next

        } 
        return this.head
   }
    
   //Dups
   dups(){
    let curr = this.head
    while (curr && curr.next) {
        if (curr.val !== curr.next.val){
            curr = curr.next
        }else{
            curr.next = curr.next.next
            this.length -- 
        }
    }
    
   }

   undups(){
    let curr = this.head
    let prev = null
    let uqset = new Set()
    if(!this.head){
        return this
    }
    while (curr !== null){
        if(!uqset.has(curr.val)){
              uqset.add(curr.val)
              prev = curr
              curr = curr.next
        }else{
            prev.next = curr.next
            curr = curr.next
            this.length -- 
        }
    }
   }

   detectCyc(){
        let slow = this.head
        let fast = this.head
        let entry = this.head
        while(fast !== null && fast.next !== null){
            slow = slow.next 
            fast = fast.next.next 
            if(slow === fast){
                break;
            }
        
        }
        if(fast === null || fast.next === null){
            return null
        }
        while(entry !== slow){
            entry =entry.next 
            slow = slow.next 
        }

        return entry
   }


    }
   

/*
// Test Cases
let first = new SinglyLinkedList(20);
first.push(25);
first.push(30);
console.log("After Push:");
first.print(); // Expected Output: 20 -> 25 -> 30

first.pop();
console.log("After Pop:");
first.print(); // Expected Output: 20 -> 25

first.unshift(15);
console.log("After Unshift:");
first.print(); // Expected Output: 15 -> 20 -> 25

first.shift();
console.log("After Shift:");
first.print();


console.log(first.get(1)); // Expected Output: Node { val: 20, next: Node { val: 30, next: null } }
console.log(first.get(0));

console.log(first.set(0,9));
first.print()

console.log(first.insert(1,55));
first.print()



console.log(first.reverse());
first.print()

console.log(first.middleelement())*/

let first = new SinglyLinkedList(10);
first.push(1);
first.push(2);
first.push(3);
first.tail.next = first.head.next

//console.log("Middle Element:",  first.middleelement()?.val);// Expected Output: 30
//console.log("Head:", first.reverselist())
//console.log(first.undups());
//first.print()
console.log(first.detectCyc())