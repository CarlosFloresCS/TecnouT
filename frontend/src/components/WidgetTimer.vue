<template>
  <div class="pomodoro-timer light">
    <div class="timer-state">
      <span class="timer-countdown">15:00</span>
      <div class="timer-actions">
        <div class="start-timer">
          <div class="lifeat-button action light">
            <button type="button">
              <span class="lifeat-button-visual"
                ><span class="lifeat-button-text">Start</span></span
              >
            </button>
          </div>
        </div>
        <div class="reset-timer">
          <div class="lifeat-button action light">
            <button type="button">
              <span class="lifeat-button-visual">
                <span class="lifeat-button-icon">
                  <img
                    src="https://img.icons8.com/material-outlined/24/null/available-updates.png"
                  />
                </span>
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="timer-selections">
      <span class="timer-option">
        <div class="lifeat-button action light">
          <button type="button">
            <span class="lifeat-button-visual">
              <span class="lifeat-button-text">Pomodoro</span>
            </span>
          </button>
        </div>
      </span>
      <span class="timer-option">
        <div class="lifeat-button action light">
          <button type="button">
            <span class="lifeat-button-visual">
              <span class="lifeat-button-text">Short Break</span>
            </span>
          </button>
        </div>
      </span>
      <span class="timer-option">
        <div class="lifeat-button action light">
          <button type="button">
            <span class="lifeat-button-visual">
              <span class="lifeat-button-text">Long Break</span>
            </span>
          </button>
        </div>
      </span>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped></style>
