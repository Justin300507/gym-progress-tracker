import React, { useState, useEffect } from 'react';
import Header from '../components/Header';
import Sidebar from '../components/Sidebar';
import { requestNotificationPermission } from '../utils/notifications';

const SettingsPage = ({ API }) => {
  const [notifStatus, setNotifStatus] = useState(null);
  const [reminderEnabled, setReminderEnabled] = useState(false);
  const [reminderTime, setReminderTime] = useState('');

  useEffect(() => {
    const fetch = async () => {
      try {
        const res = await API.get('/users/me');
        setReminderEnabled(res.data.reminder_enabled);
        setReminderTime(res.data.reminder_time || '');
      } catch (e) {}
    };
    fetch();
  }, [API]);

  const saveSettings = async () => {
    try {
      await API.patch('/users/me', { reminder_enabled: reminderEnabled, reminder_time: reminderTime });
    } catch (e) {}
  };

  return (
    <div className="flex min-h-screen bg-slate-50 dark:bg-slate-900">
      <Sidebar />
      <main className="ml-56 flex-1 p-6 overflow-auto">
        <Header />
        <h2 className="text-2xl font-semibold text-slate-900 dark:text-white mb-4">Settings</h2>
        <div className="space-y-4">
          <button onClick={async () => { const r = await requestNotificationPermission(); setNotifStatus(r); }} className="bg-orange-600 hover:bg-orange-700 text-white font-medium py-2 px-4 rounded flex items-center gap-1.5">
            Enable Notifications
          </button>
          <div className="flex items-center gap-2">
            <label className="text-sm font-medium text-slate-700 dark:text-slate-300">Reminder Enabled</label>
            <input type="checkbox" checked={reminderEnabled} onChange={e => setReminderEnabled(e.target.checked)} />
          </div>
          {reminderEnabled && (
            <div className="space-y-1">
              <label className="text-xs font-medium text-slate-700 dark:text-slate-300">Reminder Time</label>
              <input type="time" value={reminderTime} onChange={e => setReminderTime(e.target.value)} className="input" />
            </div>
          )}
          <button onClick={saveSettings} className="bg-orange-600 hover:bg-orange-700 text-white font-medium py-2 px-4 rounded">Save Settings</button>
        </div>
      </main>
    </div>
  );
};

export default SettingsPage;