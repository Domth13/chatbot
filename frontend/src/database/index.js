import axios from "axios";

const API = "http://localhost:8000"

const client = axios.create({
    baseURL: API
})

export async function fetchResponse(query) {
    console.log('test...')
    try {
        const endpoint = `/answer/${query}`
        const response = await client.get(endpoint)
        console.log(response)
        return response.data.response.response
        
    } catch (error) {
        console.log(error)
    }
}

export async function fetchConversation() {
    console.log('testConversation')
    try {
        const endpoint = `/conversations`
        const response = await client.get(endpoint)
        console.log(response)
        if (response.data === "No conversations in database") {
            return
        }
        const conversation = response.data.reduce((acc, curr) => {
            acc.user_msg.push(curr.user_msg)
            acc.bot_msg.push(curr.bot_msg)
            return acc
        }, { user_msg: [] , bot_msg: []})
        console.log(conversation)
        return conversation
        
    } catch (error) {
        console.log(error)
    }
}

export async function deleteConversations() {
    try {
        const endpoint = `/conversations`
        const response = await client.delete(endpoint)
        console.log(response)

    } catch (error) {
        console.log(error)
    }
}