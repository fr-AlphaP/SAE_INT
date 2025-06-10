fetch('animations.json')
  .then(response => response.json())
  .then(animations => {
    animations.forEach(({ selector, animation, duration, iteration }) => {
      const elements = document.querySelectorAll(selector);
      elements.forEach(el => {
        const animate = () => {
          el.style.animation = `${animation} ${duration}`;
        };
        if (iteration === 'hover') {
          el.addEventListener('mouseenter', animate);
        } else {
          el.style.animation = `${animation} ${duration} ${iteration}`;
        }
      });
    });
  })
  .catch(err => console.error('Animation load failed', err));

