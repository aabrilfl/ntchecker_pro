import {
  ADD_NOTIFICATION,
  GET_NOTIFICATION,
  DELETE_NOTIFICATION,
  UPDATE_NOTIFICATION,
  CLEAR_NOTIFICATIONS
} from "../actions/types.js";

const initialState = {
  notifications: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_NOTIFICATION:
      return {
        ...state,
        notifications: action.payload
      };
    case UPDATE_NOTIFICATION:
    case DELETE_NOTIFICATION:
      return {
        ...state,
        notifications: state.notifications.filter(
          notification => notification.id !== action.payload
        )
      };
    case ADD_NOTIFICATION:
      return {
        ...state,
        notifications: [...state.notifications, action.payload]
      };
    case CLEAR_NOTIFICATIONS:
      return {
        ...state,
        notifications: []
      };
    default:
      return state;
  }
}
