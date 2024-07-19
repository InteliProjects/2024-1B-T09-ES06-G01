<template>
  <div class="profile-info">
    <div class="picture-div">
      <img :src="picture" alt="Profile picture" />
    </div>
    <div class="info">
      <p class="name">{{ name }}</p>
      <p class="enterprise">{{ enterprise }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileInfo",
  props: {
    picture: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
    enterprise: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped lang="scss">
.profile-info {
  display: flex;
  gap: 29px;
  align-items: center;

  .picture-div {
    border-radius: 50%;
    overflow: hidden;
    background-color: black;

    img {
      width: 54px;
      height: 54px;
    }
  }

  .info {
    color: white;
    font-size: 24px;
    font-weight: 600;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
}
</style>
