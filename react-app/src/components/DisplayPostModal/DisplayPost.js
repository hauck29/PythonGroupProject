import React, { useState } from "react";
// import { useSelector } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import "./DisplayPost.css";

import { deletePost, editPost } from "../../store/posts";

import Comment from "../Comments/Comments";
import CommentForm from "../Comments/CommentForm";

import like from "../NavigationBar/images/like.png";

function DisplayPost({ postId, setShowModal }) {
  const sessionUser = useSelector((state) => state.session.user);
  const posts = useSelector((state) => state.posts);
  const [editable, isEditable] = useState(false);
  // const [isPostLoaded, setIsPostLoaded] = useState(false);
  const post = posts[postId];
  const [description, setDescription] = useState(post.description);
  const dispatch = useDispatch();
  const post_likes = useSelector((state) => state.posts[postId].likes)
  const total_likes = new Set(post_likes.filter((like) => like[2] === true).map((like) => like[0]))

  const handleEdit = async (id, description) => {
    dispatch(editPost(id, description));
    isEditable(false);
  };

  const handleDelete = async (id) => {
    dispatch(deletePost(id));
    setShowModal(false);
  };
  // if (isPostLoaded) {
  //   const editableDescription = document.getElementById(
  //     "post-description-edit"
  //   );
  //   isEditable("true");
  //   editableDescription.addEventListener("focusout", async (e) => {
  //     e.preventDefault();
  //     setDescription(editableDescription.innerHTML());
  //     handleEdit(postId, description);
  //   });
  // }

  // useEffect(() => {
  //   setIsPostLoaded(true);
  // }, []);

  return (
    <>
      <div id="post-modal-container">
        <div id="post-modal-container-content">
          <div id="post-modal-container-content-2">
            <div id="post-modal-container-content-3">
              <div id="post-modal-container-content-4">
                <div id="post-modal-image-container">
                  <div id="post-modal-image-wrapper">
                    <div id="inner-div">
                      <img className="display-photo" src={post["photos"]} alt=""></img>
                    </div>
                  </div>
                </div>
                <div id="post-modal-right-container">
                  <div id="post-modal-right-container-2">
                    <div id="post-modal-right-container-3">
                      <div id="top-right-container">
                        <div id="top-right-container-2">
                          <header id="post-modal-header">
                            <div id="profile-pic-holder">
                              <div id="profile-pic-holder-2">
                                <a id="profile-pic-link">
                                  <img id="top-right-container-img"
                                    src={post.profile_image} alt="">
                                  </img>
                                </a>
                              </div>
                            </div>
                            <div id="top-right-header-text-container">
                              <div id="header-text-wrapper">
                                <div id="header-text-wrapper-2">
                                  <span id="header-text-span">
                                    <a id="posting-user-link">
                                      {post.username}
                                    </a>
                                  </span>
                                </div>
                              </div>
                            </div>
                          </header>
                          <div id="post-edit-buttons-container">
                            {post.user_id === sessionUser.id && (
                              <button className="postBtn" onClick={() => isEditable(true)}>
                                Edit
                              </button>
                            )}{" "}
                            {editable && (
                              <div className="edit-post">
                                <textarea
                                  value={description}
                                  onChange={(e) => setDescription(e.target.value)}
                                  className="edit-description-input"
                                />
                                <button
                                  className="postBtn"
                                  onClick={() => handleEdit(postId, description)}
                                >
                                  Submit
                                </button>
                                <button className="postBtn" onClick={() => isEditable(false)}>
                                  Cancel
                                </button>
                              </div>
                            )}
                            {post.user_id === sessionUser.id && (
                              <button
                                className="postBtn"
                                onClick={() => handleDelete(postId)}
                              >
                                Delete
                              </button>
                            )}
                          </div>
                        </div>
                      </div>
                      <div id="right-section-main">
                        <section id="like-button-section">
                          <span id="post-like-button-container">
                            <button id="post-like-button">
                              <div id="post-like-button-inner-div">
                                <span id="post-like-button-inner-span">
                                  <img id="post-like-button-img" src={like} alt=""></img>
                                </span>
                              </div>
                            </button>
                          </span>
                        </section>
                        <section id="like-count-section">
                          <div id="like-count-container">
                            <div id="like-count-container-2">
                              <span id="like-count-span">
                                {total_likes.size} {total_likes.size === 1 ? "like" : "likes"}
                              </span>
                            </div>
                          </div>
                        </section>
                        <div id="right-section-description-and-comments">
                          <div id="right-section-description-and-comments-2">
                            <div id="post-description-container">
                              <li id="post-description-container-2">
                                <div id="post-description-container-3">
                                  <div id="post-description-container-4">
                                    <div id="post-description-pic-container">
                                      <div id="post-description-pic-wrapper">
                                        <a id="post-description-pic-link">
                                          <img id="post-description-pic-img" src={post.profile_image} alt=""></img>
                                        </a>
                                      </div>
                                    </div>
                                    <div id="post-description-text-container">
                                      <h2 id="post-description-text-username">
                                        <div id="post-description-text-username-2">
                                          <span id="post-description-text-username-span">
                                            <a id="post-description-text-username-link">
                                              {post.username}
                                            </a>
                                          </span>
                                        </div>
                                      </h2>
                                      <span id="post-description-text-span">{post.description}</span>
                                      {/* <div id="post-description-timestamp-container">
                                        <div id="post-description-timestamp-container-2">
                                          <time id="post-description-timestamp">[timestamp]</time>
                                        </div>
                                      </div> */}
                                    </div>
                                  </div>
                                </div>
                              </li>
                            </div>
                            <div>
                              <Comment post_id={postId} />
                            </div>
                          </div>
                        </div>
                        <div id="post-timestamp-section">
                          <a id="post-timestamp-link">
                            <time id="post-timestamp">
                              {post.createdAt.split(" ").slice(0, 4).join(" ")}
                            </time>
                          </a>
                        </div>
                        <section id="add-comment-section">
                          <CommentForm pid={post.id} />
                        </section>
                      </div>

                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
export default DisplayPost;
