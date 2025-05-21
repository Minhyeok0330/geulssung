export function moveToStep(stepNumber) {
    const totalSteps = 5;

    for (let i = 1; i <= totalSteps; i++) {
    const btn = document.getElementById(`step-${i}`);
    btn.classList.remove('step-completed', 'step-current', 'step-default');

    if (i < stepNumber) {
      btn.classList.add('step-completed');
    } else if (i === stepNumber) {
      btn.classList.add('step-current');
    } else {
      btn.classList.add('step-default');
    }
}

  // 실제 스텝 전환 동작은 여기에 추가
  // 예: document.getElementById(`step-content-${stepNumber}`).scrollIntoView();
}