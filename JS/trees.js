class Node{
    constructor(val){
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class BST{
    constructor(){
        this.root = null
    }
    display(){

    }
    insertn(val){
        const newNode = new Node(val)
        let temp = this.root
        if(this.root === null){
            this.root = newNode
            return this
        }
        while(true){
            if(newNode.val === temp.val){return undefined}
            if(newNode.val < temp.val){
                if(temp.left === null){
                    temp.left = newNode
                    return this
                }
                temp = temp.left
            }else{
                if(temp.right === null){
                    temp.right = newNode
                    return this
                }
                temp = temp.right
            }
        }
    }
    find(val){
        if(this.root === null) return false
        let temp = this.root
        while(temp){
            if(val < temp.val){
                temp = temp.left
            }else{
                if(val > temp.val){
                    temp = temp.right
                }else{
                    return true
                }
            }
            return false
        }
    }


}
let first = new BST();
first.insertn(10)
first.insertn(22)