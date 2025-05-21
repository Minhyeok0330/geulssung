export function showGenres(category) {
// 글쓰기 도우미(F/T) 선택 시 장르 선택 영역 표시
    document.getElementById('genre-logic').style.display = category === 'logic' ? 'block' : 'none';
    document.getElementById('genre-emotion').style.display = category === 'emotion' ? 'block' : 'none';

    const all = ['column', 'analysis', 'essay', 'poem'];
    all.forEach(id => {
      const guide = document.getElementById(`guide-${id}`);
      if (guide) guide.style.display = 'none';

      const prompt = document.getElementById(`prompt-${id}`);
      if (prompt) prompt.style.display = 'none';
    });
  }