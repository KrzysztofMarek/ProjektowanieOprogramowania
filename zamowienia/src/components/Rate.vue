<template>
    <v-container>
        <div id="add-rating-stars-container">
            <img :src="'/stars/'+currentRating+'.png'" class="img-responsive" id="rating-stars"/>
            <div class="add-rate" id="add-rate-1"></div>
            <div class="add-rate" id="add-rate-2"></div>
            <div class="add-rate" id="add-rate-3"></div>
            <div class="add-rate" id="add-rate-4"></div>
            <div class="add-rate" id="add-rate-5"></div>
            <div class="add-rate" id="add-rate-6"></div>
            <div class="add-rate" id="add-rate-7"></div>
            <div class="add-rate" id="add-rate-8"></div>
            <div class="add-rate" id="add-rate-9"></div>
            <div class="add-rate" id="add-rate-10"></div>
        </div>
    </v-container>
</template>

<script>

export default {
    name: "Rate",
    data: () => ({
        currentRating: 0
    }),
    mounted() {
        this.setRatingSystem();
    },
    methods: {
      setRatingSystem: function () {
        var self = this;
        for (var i = 1; i <= 10; i++) {
            (function () {
                var k = i;
                var starObject = document.getElementById("add-rate-" + i);
                if (starObject != null) {
                    starObject.onclick = function () {
                        self.currentRating = k;
                    }
                }
            }());
        }
      },
      setRating: function(rating){
          this.currentRating = rating;
      }
    }
}
</script>

<style>
#add-rating-stars-container {
    height: 35px;
    min-width: 265px;
    position: relative;
    margin-bottom: 5px;
}

#rating-stars {
    height: 35px;
    width: 175px;
    position: absolute;
    left: 0;
    top: 0;
}

.add-rate {
    height: 35px;
    width: 17.5px;
    float: left;
    position: relative;
    top: 0;
    cursor: pointer;
}

#post-rating {
    width: 85px;
    height: 35px;
    position:absolute;
    background-color: #b62020;
    color: white;
    top: 0;
    right: 0;
}


</style>
