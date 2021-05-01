const rr ={}
rr['0']=0

console.log(rr)
let ss = "0"
if(ss in rr){
    console.log(rr,"pp")
}




This is a demo task.

Write a function:

function solution(A);

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].



// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)

    const values = {}
    let st=A.length

    for(let i=0;i<st;i++){
        values[A[i]]=A[i]
    }

    let num = 1 
    let chk = false

    for(let i=0;i<st;i++){
       if(num in values){
           num+=1
           chk=true
       }
       
    }


    if(chk == false){
        return 1
    }else if(num == st){
        return num+1
    }else{
        return num
    }


}

import React, {useState, useEffect} from 'react';
import axios from 'axios';

const BASE_URI  = 'https://example.com/api/items'
const DebouncedTimeOut = 500
const AutoComplete = ({onSelectItem}) => {
    const [term, setTerm] = useState('')
    const [loading, setLoading] = useState(false)
    const [debounceterm, setDebounceTerm] = useState(term)
    const [responses, setResponses] = useState([])

    useEffect(()=>{
        const timedOut = setTimeout(()=>{
            setDebounceTerm(term)
        }, DebouncedTimeOut)
        return(()=>{
            clearTimeout(timedOut)
        })
    },[term])
    
    useEffect(() =>{
        const search = async () =>{
            try{
                setResponses([])
                
              if(debounceterm !== ''){
                  setLoading(true)
                    const response = await axios.get(BASE_URI,
                {
                    params: {
                        q:debounceterm
                    }
                })
                setLoading(false) 
                setResponses(response.data)
              }
            
            }catch(err){
                //THe question didn't say what to do with the error. So I decided to just log it since it is assumed to not fail
                console.log({error: 'Api Request Failed'})
            }
        }
        
        search()
    },[debounceterm])
    
    
    const renderResponse = () =>{
        if(responses.length>0){
            return (
                responses.map((response,index)=>{
                    return <a onClick={() => onSelectItem(response)} key={index} class="list-item">{response}</a>
                })
            )
        }
    }
   
    return(
        
            <div className='wrapper'>
                <div className={`control ${loading ? 'is-loading' : ''}`}>
                        <input className='input' type='text' value={term} onChange={(e)=>setTerm(e.target.value)} />
                </div>
                {responses.length >0 ? <div className='list'>{renderResponse()}</div> : <div className='list'></div>}
                
            </div>
            
    
    )
    
}
export default AutoComplete



import cx from 'classnames';
import { Component } from 'react';

export default class LikeDislike extends Component {
    
    state  = {
        likeCount : 100,
        dislikeCount : 25,
        like : false,
        dislike : false
    }
    
    handleLike = () => {

        if(this.state.dislike){
            this.setState({
                dislikeCount : this.state.dislikeCount-1,
                dislike : !this.state.dislike
        })
        }

        this.setState({
            like : !this.state.like
        },
        ()=>{
             if(this.state.like){
            this.setState({
                likeCount : this.state.likeCount+1
        })
        }else{
            this.setState({
                likeCount : this.state.likeCount-1
        })
        }
        })

    }


    handleDisLike = () => {

        if(this.state.like){
            this.setState({
                likeCount : this.state.likeCount-1,
                like : !this.state.like
        })
        }

        this.setState({
            dislike : !this.state.dislike
        },
        ()=>{
             if(this.state.dislike){
            this.setState({
                dislikeCount : this.state.dislikeCount+1
        })
        }else{
            this.setState({
                dislikeCount : this.state.dislikeCount-1
        })
        }
        })

    }



    
    render() {



        return (
            <>
                
                <style>{`
                    .like-button, .dislike-button {
                        font-size: 1rem;
                        padding: 5px 10px;
                        color:   #585858;
                    }

                    .liked, .disliked {
                        font-weight: bold;
                        color: #1565c0;
                    }
                `}</style>


                <div>
                    <button onClick={this.handleLike} className={`like-button ${this.state.like ? "liked" : ""}`}>Like | <span className="likes-counter">{this.state.likeCount}</span></button>
                    <button onClick={this.handleDisLike} className={`dislike-button ${this.state.dislike ? "disliked" : ""}`}>Dislike | <span className="dislikes-counter">{this.state.dislikeCount}</span></button>
                </div>


            </>
        );
    }
}




