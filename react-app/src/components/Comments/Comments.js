import React, { useEffect, useState } from "react";
import { getAllComments } from "../../store/comments";
import { useSelector, useDispatch } from "react-redux";
import { NavLink } from "react-router-dom";
// import './CommentForm.css'
import { updateAComment, deleteAComment } from "../../store/comments";
// import CommentForm from "./CommentForm";
import './Comments.css';

const Comment = ({ post_id }) => {
  const sessionUser = useSelector((state) => state.session.user);
  const comments = useSelector((state) => Object.values(state.comments));
  const [editableComment, setEditableComment] = useState(false);
  const dispatch = useDispatch();
  const [commContent, setCommContent] = useState("");

  const handleEdit = async (pid, id, content) => {
    dispatch(updateAComment(pid, id, content));
    setEditableComment(false);
  };
  useEffect(() => {
    dispatch(getAllComments(post_id));
  }, [dispatch, post_id]);

  const handleDelete = async (pid, id) => {
    dispatch(deleteAComment(pid, id));
    setEditableComment(false);
  };



  return (
    <>
      {comments?.reverse().map(({ id, user_id, content, username, profile_image }) => (
        <ul className="comment-container" key={id}>
          <div className="comment-container-2">
            <li className="comment-container-3">

              <div className="comment-container-4">
                <div className="comment-container-5">
                  <div className="comment-pic-container">
                    <div className="comment-pic-container-2">
                      <a className="comment-pic-link">
                        <img className="comment-pic-img" src={profile_image} alt=""></img>
                      </a>
                    </div>
                  </div>
                  <div className="comment-text-container">
                    <h3 className="comment-text-username">
                      <div className="comment-text-username-2">
                        <span className="comment-text-username-span">
                          <NavLink className="comment-text-username-link" to={`/users/${user_id}`}>
                            {username}
                          </NavLink>
                        </span>
                      </div>
                    </h3>
                    <span className="comment-text-span">{content}</span>
                    {/* <div className="comment-timestamp-container">
                      <div className="comment-timestamp-container-2">
                        <time>[timestamp]</time>
                      </div>
                    </div> */}
                  </div>
                </div>
                {sessionUser.id === user_id && (
                  <div className="comment-edit-buttons">
                    <button className='postBtn' onClick={() => setEditableComment(true)}>Edit</button>
                    <button className='postBtn' onClick={() => { handleDelete(post_id, id,) }}>Delete</button>
                  </div>
                )}
              </div>

              {editableComment && (
                <>
                  <input
                    className="edit-comment-field"
                    defaultValue={content}
                    type="text"
                    onChange={(e) => setCommContent(e.target.value)}
                  ></input>
                  <button className='postBtn' onClick={() => handleEdit(post_id, id, commContent)}>
                    Submit
                  </button>
                </>
              )}



            </li>
          </div>
        </ul>
      ))}
    </>
  );
};

export default Comment;
