<template>
  <dialog ref="modalElement">
    <div>
      <button class="close" @click="$emit('closeModal')"><h4>X</h4></button>
      <h1>This is Your Room Code {{ roomCode }}<br /></h1>
      Waiting for someone to join
    </div>
  </dialog>
</template>

<script setup>
import { defineProps, ref, onMounted } from "vue";

const { roomCode } = defineProps({
  roomCode: {
    type: String,
    required: true,
  },
});

const modalElement = ref(null);
onMounted(() => {
  modalElement.value.showModal();
});
</script>

<style scoped>
dialog {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 2rem;
}
.close {
  position: fixed;
  top: 0.1rem;
  right: 0.1rem;
  cursor: pointer;
  font-size: 1.1rem;
  width: 1.3rem;
}
</style>
