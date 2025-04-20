<template>
    <div class="container hero-container">
        <div class="hero">
            <main>
                <h1>Catch line</h1>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, illum.</p>
                <div class="btn-container">
                    <button @click="createRoom">Create Room</button>
                    <button @click="joinRoom">Join Room</button>
                </div>
            </main>
        </div>
    </div>
</template>

<script setup>


const createRoom = () => {
    const ws = new WebSocket('ws://localhost:8000/rooms/create-room/');
    ws.onopen = () => {
        console.log('connected');
        
    }
    ws.onmessage = (e) => {
        const data = JSON.parse(e.data);
        console.log(data);
    }
    
}
const joinRoom = () => {
    
}



</script>

<style scoped>
.hero-container{
    height: 100dvh;
    padding-top: clamp(2rem, 5vw, 3.2rem);;
}

.hero{
    width: 100%;
    height: 100%;
    background-color: cadetblue;
    display: grid;
    place-items: center;
}

.btn-container{
    width: 100%;
    display: flex;;
    gap: 1.5rem;
}
.btn-container button{
    flex: 1 0 auto;
    font-size: 1rem;
    padding-block: .5rem;
}



</style>