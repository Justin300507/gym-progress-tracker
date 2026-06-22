import React, { useEffect } from "react";
import { subscribeToNotifications, unsubscribeFromNotifications } from "../utils/notifications";

/**
 * Notifications component
 * -----------------------
 * Registers a listener for real‑time notifications when it mounts
 * and cleans up the listener on unmount. It does not render any UI itself -
 * the actual visual representation is handled elsewhere (e.g., a toast library).
 */
const Notifications = () => {
  useEffect(() => {
    const handleNotification = (payload) => {
      console.log("Received notification:", payload);
    };

    subscribeToNotifications(handleNotification);

    return () => {
      unsubscribeFromNotifications(handleNotification);
    };
  }, []);

  // No visual output - the utils library (or placeholder) handles UI.
  return null;
};

export default Notifications;
