import React from 'react';
import { Dumbbell } from 'lucide-react';
import { Link } from 'react-router-dom';

const WorkoutCard = ({ workout }) => {
  return (
    <Link to={`/workouts/${workout.id}`} className="bg-white dark:bg-slate-800 rounded-xl border border-slate-100 dark:border-slate-700 p-4 flex items-center justify-between hover:shadow-sm transition-shadow">
      <div className="flex items-center gap-3">
        <div className="w-9 h-9 rounded-lg bg-orange-50 dark:bg-orange-900/30 flex items-center justify-center">
          <Dumbbell size={18} className="text-orange-600" />
        </div>
        <div>
          <p className="text-sm font-semibold text-slate-900 dark:text-white">{new Date(workout.date).toLocaleDateString()}</p>
          <p className="text-xs text-slate-500 dark:text-slate-400">{workout.notes || 'No notes'}</p>
        </div>
      </div>
    </Link>
  );
};

export default WorkoutCard;