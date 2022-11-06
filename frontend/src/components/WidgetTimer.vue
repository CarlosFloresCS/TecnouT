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

<style scoped>
.pomodoro-timer.light {
  background: #fcfcfc;
  color: #4e4e4e;
}
.pomodoro-timer {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 10px 0;
}
.timer-state {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.timer-countdown {
  font-size: 54px;
  line-height: 50px;
  padding-left: 14px;
}
.timer-state .timer-actions {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-self: center;
}
timer-state .timer-actions .start-timer .lifeat-button {
  border: 1.5px solid #4e4e4e;
  border-radius: 14px;
  padding: 6px 25px;
}

.lifeat-button {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  height: auto;
  min-height: 36px;
  max-height: 36px;
  width: inherit;
}
lifeat-button button {
  border: 0;
  padding: 0 5px;
  font-size: 16px;
  font-family: "CircularStd";
}
.lifeat-button .lifeat-button-visual {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
}
</style>
