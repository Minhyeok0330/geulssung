export function articleSource(value) {
    const all = ['column', 'analysis', 'essay', 'poem'];

    // 모든 가이드/글감 영역 숨기기
    all.forEach(id => {
      const guide = document.getElementById(`guide-${id}`);
      if (guide) guide.style.display = 'none';

      const prompt = document.getElementById(`prompt-${id}`);
      if (prompt) prompt.style.display = 'none';
    });

    // 선택된 장르의 guide 영역 보여주기
    const guideTarget = document.getElementById(`guide-${value}`);
    if (guideTarget) guideTarget.style.display = 'block';

    // 선택된 장르의 글감 버튼 영역 보여주기
    const promptTarget = document.getElementById(`prompt-${value}`);
    if (promptTarget) promptTarget.style.display = 'block';
  }