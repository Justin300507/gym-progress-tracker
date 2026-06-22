// ForgeAI Push Notification Utilities
// Local (scheduled) notifications — no server required

export const requestNotificationPermission = async () => {
  if (!('Notification' in window)) return 'unsupported';
  if (Notification.permission === 'granted') return 'granted';
  if (Notification.permission === 'denied') return 'denied';
  const result = await Notification.requestPermission();
  return result;
};

export const showNotification = (title, options = {}) => {
  if (Notification.permission !== 'granted') return;
  if ('serviceWorker' in navigator && navigator.serviceWorker.controller) {
    navigator.serviceWorker.ready.then(reg => {
      reg.showNotification(title, {
        icon: '/icon-192.svg',
        badge: '/icon-192.svg',
        ...options,
      });
    });
  } else {
    new Notification(title, { icon: '/icon-192.svg', ...options });
  }
};

// Schedule a recurring daily reminder at a specific local time (HH:MM)
export const scheduleDaily = (title, body, timeHHMM = '09:00') => {
  const [hh, mm] = timeHHMM.split(':').map(Number);
  const fire = () => {
    const now = new Date();
    const next = new Date(now);
    next.setHours(hh, mm, 0, 0);
    if (next <= now) next.setDate(next.getDate() + 1);
    const delay = next - now;
    return setTimeout(() => { showNotification(title, { body }); fire(); }, delay);
  };
  return fire();
};

// One-shot notification after a delay (milliseconds)
export const scheduleOnce = (title, body, delayMs) => {
  return setTimeout(() => showNotification(title, { body }), delayMs);
};

// Budget alert — call when spending exceeds threshold
export const alertBudgetExceeded = (category, spent, budget) => {
  showNotification('Budget Alert', {
    body: `${category}: $${spent.toFixed(0)} spent of $${budget} budget`,
    tag: `budget-${category}`,
  });
};

// Workout reminder
export const alertWorkoutReminder = (workoutName = 'your workout') => {
  showNotification("Time to train!", {
    body: `Don't skip ${workoutName} today. You've got this! 💪`,
    tag: 'workout-reminder',
  });
};
