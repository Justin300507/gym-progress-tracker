import React, { useEffect, useState } from 'react';
import Header from '../components/Header';
import Sidebar from '../components/Sidebar';
import { useParams } from 'react-router-dom';
import { Dumbbell } from 'lucide-react';

const WorkoutDetailPage = ({ API }) => {
  const { id } = useParams();
  const [workout, setWorkout] = useState(null);

  useEffect(() => {
    const fetch = async () => {
      try {
        const res = await API.get(`/workouts/${id}`);
        setWorkout(res.data);
      } catch (e) {}
    };
    fetch();
  }, [API, id]);

  if (!workout) {
    return (
      <div className="flex min-h-screen bg-slate-50 dark:bg-slate-900">
        <Sidebar />
        <main className="ml-56 flex-1 p-6 overflow-auto">
          <Header />
          <p className="text-slate-500 dark:text-slate-400">Loading...</p>
        </main>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen bg-slate-50 dark:bg-slate-900">
      <Sidebar />
      <main className="ml-56 flex-1 p-6 overflow-auto">
        <Header />
        <h2 className="text-2xl font-semibold text-slate-900 dark:text-white mb-4">Workout Details</h2>
        <div className="bg-white dark:bg-slate-800 rounded-xl border border-slate-100 dark:border-slate-700 p-4 mb-4">
          <p className="text-sm font-medium text-slate-900 dark:text-white">{new Date(workout.date).toLocaleDateString()}</p>
          <p className="text-xs text-slate-500 dark:text-slate-400">{workout.notes}</p>
        </div>
        <p className="text-slate-500 dark:text-slate-400">Exercise details go here.</p>
      </main>
    </div>
  );
};

export default WorkoutDetailPage;