<template>

  <form>
    <fieldset class="dxt-fieldset">

        <legend class="dxt-legend">Legend</legend>

        <div class="dxt-margin">
            <input class="dxt-input" type="text" placeholder="Input">
        </div>

        <div class="dxt-margin">
            <select class="dxt-select">
                <option>Option 01</option>
                <option>Option 02</option>
            </select>

        </div>

        <div class="dxt-margin">
            <textarea class="dxt-textarea" rows="5" placeholder="Textarea"></textarea>
        </div>

        <div class="dxt-margin dxt-grid-small dxt-child-width-auto dxt-grid">
            <label><input class="dxt-radio" type="radio" name="radio2" checked> A</label>
            <label><input class="dxt-radio" type="radio" name="radio2"> B</label>
        </div>

        <div class="dxt-margin dxt-grid-small dxt-child-width-auto dxt-grid">
            <label><input class="dxt-checkbox" type="checkbox" checked> A</label>
            <label><input class="dxt-checkbox" type="checkbox"> B</label>
        </div>

        <div class="dxt-margin">
            <input class="dxt-range" type="range" value="2" min="0" max="10" step="0.1">
        </div>

    </fieldset>
</form>

</template>

<script>
import Logo from '~/components/Logo.vue'

export default {
  components: {
    Logo
  }
}
</script>

<style lang="sass">

</style>
