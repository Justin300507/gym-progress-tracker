import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import axios from 'axios';
import InstallPrompt from './components/InstallPrompt';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import DashboardPage from './pages/DashboardPage';
import WorkoutListPage from './pages/WorkoutListPage';
import WorkoutDetailPage from './pages/WorkoutDetailPage';
import NewWorkoutPage from './pages/NewWorkoutPage';
import PersonalRecordsPage from './pages/PersonalRecordsPage';
import StatsPage from './pages/StatsPage';
import SettingsPage from './pages/SettingsPage';

const API = axios.create({ baseURL: '' });
API.interceptors.request.use(cfg => {
  const token = localStorage.getItem('token');
  if (token) cfg.headers.Authorization = `Bearer ${token}`;
  return cfg;
});

const PrivateRoute = ({ children }) => {
  const token = localStorage.getItem('token');
  return token ? children : <Navigate to="/login" replace />;
};

const App = () => {
  return (
    <Router>
      <InstallPrompt />
      <Routes>
        <Route path="/login" element={<LoginPage API={API} />} />
        <Route path="/register" element={<RegisterPage API={API} />} />
        <Route
          path="/*"
          element={
            <PrivateRoute>
              <Routes>
                <Route path="dashboard" element={<DashboardPage API={API} />} />
                <Route path="workouts" element={<WorkoutListPage API={API} />} />
                <Route path="workouts/new" element={<NewWorkoutPage API={API} />} />
                <Route path="workouts/:id" element={<WorkoutDetailPage API={API} />} />
                <Route path="personal-records" element={<PersonalRecordsPage API={API} />} />
                <Route path="stats" element={<StatsPage API={API} />} />
                <Route path="settings" element={<SettingsPage API={API} />} />
                <Route path="*" element={<Navigate to="/dashboard" replace />} />
              </Routes>
            </PrivateRoute>
          }
        />
      </Routes>
    </Router>
  );
};

export default App;