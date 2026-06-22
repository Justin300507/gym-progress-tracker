import React, { useEffect, useState } from 'react';
import Header from '../components/Header';
import Sidebar from '../components/Sidebar';
import StatCard from '../components/StatCard';
import Chart from '../components/Chart';
import WorkoutCard from '../components/WorkoutCard';
import { Dumbbell, Activity, Flame, Trophy } from 'lucide-react';

const DashboardPage = ({ API }) => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const res = await API.get('/workouts');
        setWorkouts(res.data.slice(0, 5));
      } catch (e) {}
    };
    fetchWorkouts();
  }, [API]);

  const today = new Date().toLocaleDateString();

  return (
    <div className="flex min-h-screen bg-slate-50 dark:bg-slate-900">
      <Sidebar />
      <main className="ml-56 flex-1 p-6 overflow-auto">
        <Header />
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-2xl font-semibold text-slate-900 dark:text-white">Hello, User</h2>
          <span className="text-slate-500 dark:text-slate-400">{today}</span>
        </div>
        <div className="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 mb-6">
          <StatCard label="Total Workouts" value={workouts.length} change="+5% this week" icon={Dumbbell} />
          <StatCard label="Active Days" value="3" change="+10% this week" icon={Activity} />
          <StatCard label="Calories Burned" value="1,200" change="+8% this week" icon={Flame} />
          <StatCard label="Personal Records" value="5" change="+2% this week" icon={Trophy} />
        </div>
        <Chart API={API} />
        <section className="mt-6">
          <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-4">Recent Workouts</h3>
          {workouts.length === 0 ? (
            <p className="text-slate-500 dark:text-slate-400">No recent workouts.</p>
          ) : (
            <div className="space-y-3">
              {workouts.map(w => (
                <WorkoutCard key={w.id} workout={w} />
              ))}
            </div>
          )}
        </section>
      </main>
    </div>
  );
};

export default DashboardPage;