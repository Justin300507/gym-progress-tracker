import React, { useState } from 'react';
import { Bell } from 'lucide-react';
import { requestNotificationPermission, scheduleDaily, alertWorkoutReminder } from '../utils/notifications';

const ReminderToggle = () => {
  const [enabled, setEnabled] = useState(false);
  const toggle = async () => {
    const granted = await requestNotificationPermission();
    if (granted) {
      setEnabled(true);
      scheduleDaily(() => {
        alertWorkoutReminder('Time for your workout!');
      });
    } else {
      setEnabled(false);
    }
  };
  return (
    <button onClick={toggle} className="flex items-center gap-2 px-4 py-2 bg-orange-600 hover:bg-orange-700 text-white rounded-lg">
      <Bell size={16} /> {enabled ? 'Disable' : 'Enable'} Notifications
    </button>
  );
};

export default ReminderToggle;