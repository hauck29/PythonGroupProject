import { csrfFetch } from "./csrf"

// action types
const LOAD_LIKES = 'likes/LOAD_LIKES'
const ADD_LIKE = 'likes/ADD_LIKE'
const REMOVE_LIKE = 'likes/REMOVE_LIKE'

const getLikes = (likes) => ({
  type: LOAD_LIKES,
  payload: likes
});

const addLike = (like) => ({
  type: ADD_LIKE,
  payload: like
});

const removeLike = (id) => ({
  type: REMOVE_LIKE,
  payload: id
});

export const fetchLikes = () => async (dispatch) => {
  const res = await csrfFetch('/api/likes')
  if (res.ok) {
    const spots = await res.json();
    dispatch(getLikes(likes));
  } else {
    throw res;
  }
}

export const addNewReview = (data, postId) => async (dispatch) => {
  const res = await csrfFetch(`/api/posts/${postId}/likes`, {
    method: "POST",
    headers: { 'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  })
  if(res.ok) {
    const review = await res.json();
    dispatch(addLike(like))
    return review
}

}

export const deleteLike = (postId, id) => async dispatch => {
  const response = await csrfFetch(`/api/posts/${postId}/likes/${id}`, {
    method: 'PUT',
  });
  if (response.ok) {
    dispatch(removeLike(id));
  }
};

const initialState = {}

const likesReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOAD_LIKES: {

      return action.likes.reduce((likes, like) => {
        likes[like.id] = like
        return likes
      },{})
      }

    case ADD_LIKE:
      return action.like

    case REMOVE_LIKE:
      const newState = {...state};
      delete newState[action.id]
      return newState
      }
    }


    export default likesReducer