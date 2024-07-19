<template>
  <section class="users">
    <div class="users-page-back">
      <ThePageBack page="Gerenciar Usuários" />
      <button @click="openModal">
        <img src="/plus.svg" alt="Add button" />
      </button>
    </div>
    <SearchBar v-model="searchQuery" />
    <div class="users-list">
      <TheUser 
        v-for="user in filteredUsers" 
        :key="user.id" 
        :user="user" 
        @click="openEditModal(user)"
      />
    </div>
    <TheModal :isOpen="isModalOpen" @close="closeModal">
      <CreateUserForm 
        :user="selectedUser" 
        @create-user="addUser" 
        @update-user="updateUser"
        @close-modal="closeModal" 
      />
    </TheModal>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRuntimeConfig } from '#imports';
import ThePageBack from '~/components/the-page-back.vue';
import TheUser from '~/components/the-user.vue';
import TheModal from '~/components/the-modal.vue';
import CreateUserForm from '~/components/create-user-form.vue';
import SearchBar from '~/components/search-bar.vue';

const users = ref([]);
const isModalOpen = ref(false);
const searchQuery = ref('');
const selectedUser = ref(null);
const config = useRuntimeConfig();

const fetchUsers = async () => {
  try {
    const response = await $fetch('/ceos/', {
      baseURL: config.public.baseURL
    });
    users.value = response.ceos;
  } catch (error) {
    console.error('Error fetching users:', error);
  }
};

const addUser = async (newUser) => {
  try {
    // REMOVING THE ID FROM THE NEW USER
    delete newUser.id;
    const response = await $fetch('/ceos/', {
      method: 'POST',
      baseURL: config.public.baseURL,
      body: newUser
    });
    users.value.push(response);
    closeModal();
  } catch (error) {
    console.error('Error adding user:', error);
  }
};

const updateUser = async (updatedUser) => {
  try {
    const body = { ...updatedUser };
    delete body.id;
    const response = await $fetch(`/ceos/${updatedUser.id}`, {
      method: 'PUT',
      baseURL: config.public.baseURL,
      body: body
    });
    const index = users.value.findIndex(user => user.id === updatedUser.id);
    if (index !== -1) {
      users.value.splice(index, 1, response);
    }
    closeModal();
  } catch (error) {
    console.error('Error updating user:', error);
  }
};

const deleteUser = async (userId) => {
  try {
    await $fetch(`/ceos/${userId}`, {
      method: 'DELETE',
      baseURL: config.public.baseURL
    });
    users.value = users.value.filter(user => user.id !== userId);
  } catch (error) {
    console.error('Error deleting user:', error);
  }
};

const openModal = () => {
  selectedUser.value = null;
  isModalOpen.value = true;
};

const openEditModal = (user) => {
  selectedUser.value = user;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
};

const filteredUsers = computed(() => {
  return users.value.filter(user => 
    (user.nome && user.nome.toLowerCase().includes(searchQuery.value.toLowerCase())) ||
    (user.empresa && user.empresa.toLowerCase().includes(searchQuery.value.toLowerCase()))
  );
});

onMounted(() => {
  fetchUsers();
});
</script>

<style scoped lang="scss">
.users {
  padding: 0 60px;

  &-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  &-page-back {
    display: flex;
    justify-content: space-between;
    gap: 33px;
    margin-bottom: 32px;

    button {
      width: 35px;
      height: 35px;

      img {
        width: 100%;
        height: 100%;
      }
    }
  }
}
</style>
